// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取office文档在线编辑地址
 */
public class GetOfficeEditUrlRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    @NameInMap("option")
    public GetOfficeEditUrlOption option;

    @NameInMap("watermark")
    public GetOfficeEditUrlWatermark watermark;

    public static GetOfficeEditUrlRequest build(java.util.Map<String, ?> map) throws Exception {
        GetOfficeEditUrlRequest self = new GetOfficeEditUrlRequest();
        return TeaModel.build(map, self);
    }

    public GetOfficeEditUrlRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetOfficeEditUrlRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public GetOfficeEditUrlRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetOfficeEditUrlRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public GetOfficeEditUrlRequest setOption(GetOfficeEditUrlOption option) {
        this.option = option;
        return this;
    }
    public GetOfficeEditUrlOption getOption() {
        return this.option;
    }

    public GetOfficeEditUrlRequest setWatermark(GetOfficeEditUrlWatermark watermark) {
        this.watermark = watermark;
        return this;
    }
    public GetOfficeEditUrlWatermark getWatermark() {
        return this.watermark;
    }

}
