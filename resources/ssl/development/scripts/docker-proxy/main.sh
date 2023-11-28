#!/bin/bash
# set -x
set -e
set -u

## Settings
readonly RESOLVER_TLD="dev"
readonly DOCKER_VM_NAME="docker-vm"
readonly CONTAINER_NGINX="proxy_nginx"
readonly CONTAINER_DNSMASQ="proxy_dns"

readonly ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

## Flags
readonly FLAG_OSX=1
readonly FLAG_LINUX=2
readonly FLAG_DOCKER_MACHINE=4
readonly FLAG_DOCKER_BETA=8
readonly FLAG_DOCKER_UNKNOWN=16
readonly FLAG_PROXY_NGINX=32
readonly FLAG_PROXY_DNS=64

readonly BB_CONSENT_DOMAIN="bb-consent.dev"
readonly BB_CONSENT_SUBDOMAINS="api.${BB_CONSENT_DOMAIN} dashboard.${BB_CONSENT_DOMAIN} privacy.${BB_CONSENT_DOMAIN} docs.${BB_CONSENT_DOMAIN} swagger.${BB_CONSENT_DOMAIN}"
ENVIRONMENT_FLAGS=0
DOCKER_IP=127.0.0.1


function detect_flags {
  which docker > /dev/null || (echo "docker command not found"; exit 1)

  ENVIRONMENT_FLAGS=$FLAG_PROXY_NGINX
  ## OS
  case $(uname -s) in
    "Darwin")
      ENVIRONMENT_FLAGS=$ENVIRONMENT_FLAGS+$FLAG_OSX
      ENVIRONMENT_FLAGS=$ENVIRONMENT_FLAGS+$FLAG_PROXY_DNS
    ;;
    "Linux")
      ENVIRONMENT_FLAGS=$ENVIRONMENT_FLAGS+$FLAG_LINUX
    ;;
    *)
      echo "Unsupported OS"
      exit 1
    ;;
  esac

  if (((ENVIRONMENT_FLAGS & FLAG_OSX)>0)); then
      case $(docker info 2>/dev/null | sed -n "s/Operating System: \(.*\)/\1/p") in
        "Alpine Linux v"*)
          # Docker beta
          ENVIRONMENT_FLAGS=$ENVIRONMENT_FLAGS+$FLAG_DOCKER_BETA
          ;;
        "Boot2Docker "*)
          # Docker machine
          ENVIRONMENT_FLAGS=$ENVIRONMENT_FLAGS+$FLAG_DOCKER_MACHINE
          ;;
        *)
          ENVIRONMENT_FLAGS=$ENVIRONMENT_FLAGS+$FLAG_DOCKER_UNKNOWN
          ;;
      esac
  fi
}

function set_hosts {
  local host_ip=$1

  if [[ -z "${host_ip}" ]]; then
    echo "misssing host ip"
    exit 1
  fi
  sed "/# bb-consent/d" /etc/hosts | sudo tee /etc/hosts > /dev/null
  echo -e "${host_ip}\t${BB_CONSENT_SUBDOMAINS} # bb-consent" | sudo tee -a /etc/hosts > /dev/null
}

detect_flags

set_hosts "${DOCKER_IP}"

echo "Done"
exit 0
