// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * create file request
 */
public class BaseCreateFileRequest extends TeaModel {
    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // ContentMd5
    @NameInMap("content_md5")
    public String contentMd5;

    // ContentType
    @NameInMap("content_type")
    public String contentType;

    // Name
    @NameInMap("name")
    @Validation(required = true, maxLength = 1024, minLength = 1)
    public String name;

    // part_info_list
    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    // Size
    @NameInMap("size")
    public Long size;

    // Type
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    public static BaseCreateFileRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseCreateFileRequest self = new BaseCreateFileRequest();
        return TeaModel.build(map, self);
    }

    public BaseCreateFileRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public BaseCreateFileRequest setContentMd5(String contentMd5) {
        this.contentMd5 = contentMd5;
        return this;
    }
    public String getContentMd5() {
        return this.contentMd5;
    }

    public BaseCreateFileRequest setContentType(String contentType) {
        this.contentType = contentType;
        return this;
    }
    public String getContentType() {
        return this.contentType;
    }

    public BaseCreateFileRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public BaseCreateFileRequest setPartInfoList(java.util.List<UploadPartInfo> partInfoList) {
        this.partInfoList = partInfoList;
        return this;
    }
    public java.util.List<UploadPartInfo> getPartInfoList() {
        return this.partInfoList;
    }

    public BaseCreateFileRequest setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public BaseCreateFileRequest setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
