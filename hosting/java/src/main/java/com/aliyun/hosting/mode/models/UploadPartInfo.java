// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UploadPartInfo extends TeaModel {
    // etag
    @NameInMap("etag")
    public String etag;

    // PartNumber
    @NameInMap("part_number")
    @Validation(pattern = "[0-9]+")
    public Long partNumber;

    // PartSize：
    @NameInMap("part_size")
    public Long partSize;

    // upload_url
    @NameInMap("upload_url")
    public String uploadUrl;

    public static UploadPartInfo build(java.util.Map<String, ?> map) throws Exception {
        UploadPartInfo self = new UploadPartInfo();
        return TeaModel.build(map, self);
    }

    public UploadPartInfo setEtag(String etag) {
        this.etag = etag;
        return this;
    }
    public String getEtag() {
        return this.etag;
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
