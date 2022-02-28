// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * UCGetSignatureResponse
 */
public class UCGetSignatureResponse extends TeaModel {
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

    public static UCGetSignatureResponse build(java.util.Map<String, ?> map) throws Exception {
        UCGetSignatureResponse self = new UCGetSignatureResponse();
        return TeaModel.build(map, self);
    }

    public UCGetSignatureResponse setBucket(String bucket) {
        this.bucket = bucket;
        return this;
    }
    public String getBucket() {
        return this.bucket;
    }

    public UCGetSignatureResponse setCanonicalizedResource(String canonicalizedResource) {
        this.canonicalizedResource = canonicalizedResource;
        return this;
    }
    public String getCanonicalizedResource() {
        return this.canonicalizedResource;
    }

    public UCGetSignatureResponse setEndpoint(String endpoint) {
        this.endpoint = endpoint;
        return this;
    }
    public String getEndpoint() {
        return this.endpoint;
    }

    public UCGetSignatureResponse setHeaders(java.util.Map<String, ?> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, ?> getHeaders() {
        return this.headers;
    }

    public UCGetSignatureResponse setObjectKey(String objectKey) {
        this.objectKey = objectKey;
        return this;
    }
    public String getObjectKey() {
        return this.objectKey;
    }

    public UCGetSignatureResponse setSignature(String signature) {
        this.signature = signature;
        return this;
    }
    public String getSignature() {
        return this.signature;
    }

    public UCGetSignatureResponse setStrToSign(String strToSign) {
        this.strToSign = strToSign;
        return this;
    }
    public String getStrToSign() {
        return this.strToSign;
    }

}
