// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UploadPartInfo extends TeaModel {
    // content_type
    @NameInMap("content_type")
    public String contentType;

    // etag
    @NameInMap("etag")
    public String etag;

    // internal_upload_url
    @NameInMap("internal_upload_url")
    public String internalUploadUrl;

    @NameInMap("parallel_sha1_ctx")
    public SHA1CTX parallelSha1Ctx;

    // PartNumber
    @NameInMap("part_number")
    @Validation(maximum = 10000, minimum = 1)
    public Long partNumber;

    // PartSize：
    @NameInMap("part_size")
    @Validation(maximum = 5368709120D)
    public Long partSize;

    // upload_url
    @NameInMap("upload_url")
    public String uploadUrl;

    public static UploadPartInfo build(java.util.Map<String, ?> map) throws Exception {
        UploadPartInfo self = new UploadPartInfo();
        return TeaModel.build(map, self);
    }

    public UploadPartInfo setContentType(String contentType) {
        this.contentType = contentType;
        return this;
    }
    public String getContentType() {
        return this.contentType;
    }

    public UploadPartInfo setEtag(String etag) {
        this.etag = etag;
        return this;
    }
    public String getEtag() {
        return this.etag;
    }

    public UploadPartInfo setInternalUploadUrl(String internalUploadUrl) {
        this.internalUploadUrl = internalUploadUrl;
        return this;
    }
    public String getInternalUploadUrl() {
        return this.internalUploadUrl;
    }

    public UploadPartInfo setParallelSha1Ctx(SHA1CTX parallelSha1Ctx) {
        this.parallelSha1Ctx = parallelSha1Ctx;
        return this;
    }
    public SHA1CTX getParallelSha1Ctx() {
        return this.parallelSha1Ctx;
    }

    public UploadPartInfo setPartNumber(Long partNumber) {
        this.partNumber = partNumber;
        return this;
    }
    public Long getPartNumber() {
        return this.partNumber;
    }

    public UploadPartInfo setPartSize(Long partSize) {
        this.partSize = partSize;
        return this;
    }
    public Long getPartSize() {
        return this.partSize;
    }

    public UploadPartInfo setUploadUrl(String uploadUrl) {
        this.uploadUrl = uploadUrl;
        return this;
    }
    public String getUploadUrl() {
        return this.uploadUrl;
    }

}
