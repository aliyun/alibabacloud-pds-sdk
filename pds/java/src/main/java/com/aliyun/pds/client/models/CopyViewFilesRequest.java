// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Copy view files
 */
public class CopyViewFilesRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // auto_rename
    // type: boolean
    @NameInMap("auto_rename")
    public Boolean autoRename;

    // category
    @NameInMap("category")
    @Validation(required = true)
    public String category;

    @NameInMap("drive_file_list")
    public java.util.List<ShareFile> driveFileList;

    @NameInMap("referer")
    public String referer;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    // to_drive_id
    @NameInMap("to_drive_id")
    @Validation(pattern = "[0-9]+")
    public String toDriveId;

    // to_parent_file_id
    @NameInMap("to_parent_file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 4)
    public String toParentFileId;

    // to_view_id
    @NameInMap("to_view_id")
    @Validation(required = true)
    public String toViewId;

    // user_id
    @NameInMap("user_id")
    public String userId;

    // view_id
    @NameInMap("view_id")
    @Validation(required = true)
    public String viewId;

    public static CopyViewFilesRequest build(java.util.Map<String, ?> map) throws Exception {
        CopyViewFilesRequest self = new CopyViewFilesRequest();
        return TeaModel.build(map, self);
    }

    public CopyViewFilesRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CopyViewFilesRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public CopyViewFilesRequest setAutoRename(Boolean autoRename) {
        this.autoRename = autoRename;
        return this;
    }
    public Boolean getAutoRename() {
        return this.autoRename;
    }

    public CopyViewFilesRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public CopyViewFilesRequest setDriveFileList(java.util.List<ShareFile> driveFileList) {
        this.driveFileList = driveFileList;
        return this;
    }
    public java.util.List<ShareFile> getDriveFileList() {
        return this.driveFileList;
    }

    public CopyViewFilesRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public CopyViewFilesRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public CopyViewFilesRequest setToDriveId(String toDriveId) {
        this.toDriveId = toDriveId;
        return this;
    }
    public String getToDriveId() {
        return this.toDriveId;
    }

    public CopyViewFilesRequest setToParentFileId(String toParentFileId) {
        this.toParentFileId = toParentFileId;
        return this;
    }
    public String getToParentFileId() {
        return this.toParentFileId;
    }

    public CopyViewFilesRequest setToViewId(String toViewId) {
        this.toViewId = toViewId;
        return this;
    }
    public String getToViewId() {
        return this.toViewId;
    }

    public CopyViewFilesRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public CopyViewFilesRequest setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
