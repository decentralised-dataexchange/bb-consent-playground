import json

from jwcrypto import jwk, jwt



def generate_secp256r1_jwk():
    # Generate EC key pair for secp256r1 curve
    key = jwk.JWK.generate(kty="EC", crv="P-256")
    return key


def sign_jws(payload, private_key):
    # Generate JSON web signature
    key = jwk.JWK(**private_key)
    token = jwt.JWT(header={"alg": "ES256"}, claims=payload)
    token.make_signed_token(key)
    return token.serialize()

private_key = generate_secp256r1_jwk()

payload = "{\"schemaName\":\"ConsentRecord\",\"objectId\":\"2\",\"signedWithoutObjectId\":false,\"timestamp\":\"2024-01-17T10:15:07Z\",\"authorizedByIndividualId\":\"1\",\"authorizedByOtherId\":\"\",\"objectData\":\"{\\\"id\\\":\\\"2\\\",\\\"dataAgreementId\\\":\\\"2\\\",\\\"dataAgreementRevisionId\\\":\\\"659fd68befcb8216c24c2695\\\",\\\"dataAgreementRevisionHash\\\":\\\"3f0f5aef5e79afb50428ed835ad628db449c4504\\\",\\\"individualId\\\":\\\"1\\\",\\\"optIn\\\":true,\\\"state\\\":\\\"signed\\\",\\\"signatureId\\\":\\\"1\\\"}\"}"

jws_token = sign_jws(payload, private_key.export(as_dict=True))

print(
    f"Public key JWK:\n{json.dumps(private_key.export(private_key=False, as_dict=False), indent=2)}\n"
)
print(f"JWS:\n{jws_token}")


