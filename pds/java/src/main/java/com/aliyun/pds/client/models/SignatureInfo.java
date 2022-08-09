// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class SignatureInfo extends TeaModel {
    @NameInMap("bucket")
    public String bucket;

    @NameInMap("canonicalized_resource")
    public String canonicalizedResource;

    @NameInMap("endpoint")
    public String endpoint;

    @NameInMap("headers")
    public java.util.Map<String, ?> headers;

    @NameInMap("object_key")
    public String objectKey;

    @NameInMap("signature")
    public String signature;

    @NameInMap("str_to_sign")
    public String strToSign;

    public static SignatureInfo build(java.util.Map<String, ?> map) throws Exception {
        SignatureInfo self = new SignatureInfo();
        return TeaModel.build(map, self);
    }

    public SignatureInfo setBucket(String bucket) {
        this.bucket = bucket;
        return this;
    }
    public String getBucket() {
        return this.bucket;
    }

    public SignatureInfo setCanonicalizedResource(String canonicalizedResource) {
        this.canonicalizedResource = canonicalizedResource;
        return this;
    }
    public String getCanonicalizedResource() {
        return this.canonicalizedResource;
    }

    public SignatureInfo setEndpoint(String endpoint) {
        this.endpoint = endpoint;
        return this;
    }
    public String getEndpoint() {
        return this.endpoint;
    }

    public SignatureInfo setHeaders(java.util.Map<String, ?> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, ?> getHeaders() {
        return this.headers;
    }

    public SignatureInfo setObjectKey(String objectKey) {
        this.objectKey = objectKey;
        return this;
    }
    public String getObjectKey() {
        return this.objectKey;
    }

    public SignatureInfo setSignature(String signature) {
        this.signature = signature;
        return this;
    }
    public String getSignature() {
        return this.signature;
    }

    public SignatureInfo setStrToSign(String strToSign) {
        this.strToSign = strToSign;
        return this;
    }
    public String getStrToSign() {
        return this.strToSign;
    }

}
