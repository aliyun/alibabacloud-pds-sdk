// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UploadPartInfo extends TeaModel {
    /**
     * <p>content_type</p>
     */
    @NameInMap("content_type")
    public String contentType;

    /**
     * <p>etag</p>
     */
    @NameInMap("etag")
    public String etag;

    @NameInMap("internal_upload_form_info")
    public UploadFormInfo internalUploadFormInfo;

    /**
     * <p>internal_upload_url</p>
     */
    @NameInMap("internal_upload_url")
    public String internalUploadUrl;

    @NameInMap("parallel_sha1_ctx")
    public SHA1CTX parallelSha1Ctx;

    /**
     * <p>PartNumber</p>
     */
    @NameInMap("part_number")
    @Validation(maximum = 10000, minimum = 1)
    public Long partNumber;

    /**
     * <p>PartSize：</p>
     */
    @NameInMap("part_size")
    @Validation(maximum = 5368709120D)
    public Long partSize;

    @NameInMap("upload_form_info")
    public UploadFormInfo uploadFormInfo;

    /**
     * <p>upload_url</p>
     */
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

    public UploadPartInfo setInternalUploadFormInfo(UploadFormInfo internalUploadFormInfo) {
        this.internalUploadFormInfo = internalUploadFormInfo;
        return this;
    }
    public UploadFormInfo getInternalUploadFormInfo() {
        return this.internalUploadFormInfo;
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

    public UploadPartInfo setUploadFormInfo(UploadFormInfo uploadFormInfo) {
        this.uploadFormInfo = uploadFormInfo;
        return this;
    }
    public UploadFormInfo getUploadFormInfo() {
        return this.uploadFormInfo;
    }

    public UploadPartInfo setUploadUrl(String uploadUrl) {
        this.uploadUrl = uploadUrl;
        return this;
    }
    public String getUploadUrl() {
        return this.uploadUrl;
    }

}
