// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 获取office文档预览地址
 */
public class GetOfficePreviewUrlRequest extends TeaModel {
    /**
     * <p>addition_data</p>
     */
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    /**
     * <p>allow_copy</p>
     * <p>default true</p>
     */
    @NameInMap("allow_copy")
    public Boolean allowCopy;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    /**
     * <p>language</p>
     */
    @NameInMap("language")
    public String language;

    @NameInMap("option")
    public GetOfficePreviewUrlOption option;

    @NameInMap("referer")
    public String referer;

    /**
     * <p>revision_id</p>
     */
    @NameInMap("revision_id")
    public String revisionId;

    /**
     * <p>share_id, either share_id or drive_id is required</p>
     */
    @NameInMap("share_id")
    public String shareId;

    public static GetOfficePreviewUrlRequest build(java.util.Map<String, ?> map) throws Exception {
        GetOfficePreviewUrlRequest self = new GetOfficePreviewUrlRequest();
        return TeaModel.build(map, self);
    }

    public GetOfficePreviewUrlRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public GetOfficePreviewUrlRequest setAllowCopy(Boolean allowCopy) {
        this.allowCopy = allowCopy;
        return this;
    }
    public Boolean getAllowCopy() {
        return this.allowCopy;
    }

    public GetOfficePreviewUrlRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetOfficePreviewUrlRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public GetOfficePreviewUrlRequest setLanguage(String language) {
        this.language = language;
        return this;
    }
    public String getLanguage() {
        return this.language;
    }

    public GetOfficePreviewUrlRequest setOption(GetOfficePreviewUrlOption option) {
        this.option = option;
        return this;
    }
    public GetOfficePreviewUrlOption getOption() {
        return this.option;
    }

    public GetOfficePreviewUrlRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public GetOfficePreviewUrlRequest setRevisionId(String revisionId) {
        this.revisionId = revisionId;
        return this;
    }
    public String getRevisionId() {
        return this.revisionId;
    }

    public GetOfficePreviewUrlRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
