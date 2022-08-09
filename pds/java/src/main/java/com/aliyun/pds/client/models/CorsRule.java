// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class CorsRule extends TeaModel {
    // AllowedHeader
    @NameInMap("allowed_header")
    public java.util.List<String> allowedHeader;

    // AllowedMethod
    @NameInMap("allowed_method")
    public java.util.List<String> allowedMethod;

    // AllowedOrigin
    @NameInMap("allowed_origin")
    public java.util.List<String> allowedOrigin;

    // ExposeHeader
    @NameInMap("expose_header")
    public java.util.List<String> exposeHeader;

    // MaxAgeSeconds
    @NameInMap("max_age_seconds")
    public Long maxAgeSeconds;

    public static CorsRule build(java.util.Map<String, ?> map) throws Exception {
        CorsRule self = new CorsRule();
        return TeaModel.build(map, self);
    }

    public CorsRule setAllowedHeader(java.util.List<String> allowedHeader) {
        this.allowedHeader = allowedHeader;
        return this;
    }
    public java.util.List<String> getAllowedHeader() {
        return this.allowedHeader;
    }

    public CorsRule setAllowedMethod(java.util.List<String> allowedMethod) {
        this.allowedMethod = allowedMethod;
        return this;
    }
    public java.util.List<String> getAllowedMethod() {
        return this.allowedMethod;
    }

    public CorsRule setAllowedOrigin(java.util.List<String> allowedOrigin) {
        this.allowedOrigin = allowedOrigin;
        return this;
    }
    public java.util.List<String> getAllowedOrigin() {
        return this.allowedOrigin;
    }

    public CorsRule setExposeHeader(java.util.List<String> exposeHeader) {
        this.exposeHeader = exposeHeader;
        return this;
    }
    public java.util.List<String> getExposeHeader() {
        return this.exposeHeader;
    }

    public CorsRule setMaxAgeSeconds(Long maxAgeSeconds) {
        this.maxAgeSeconds = maxAgeSeconds;
        return this;
    }
    public Long getMaxAgeSeconds() {
        return this.maxAgeSeconds;
    }

}
