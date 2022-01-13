// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * create_share_link request
 */
public class CreateShareLinkRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // category
    @NameInMap("category")
    public String category;

    // description
    @NameInMap("description")
    public String description;

    // 多drive使用该字段，view分享支持跨drive，使用该字段，如果为空，则是分享view下所有文件
    @NameInMap("drive_file_list")
    public java.util.List<ShareFile> driveFileList;

    // 单drive使用以下字段，文件共享目前使用该字段
    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // enable_file_changed_notify
    @NameInMap("enable_file_changed_notify")
    public Boolean enableFileChangedNotify;

    // expiration
    @NameInMap("expiration")
    public String expiration;

    // file_id
    @NameInMap("file_id")
    public String fileId;

    // file_id_list
    @NameInMap("file_id_list")
    public java.util.List<String> fileIdList;

    // file_path_list
    @NameInMap("file_path_list")
    public java.util.List<String> filePathList;

    // filter_group
    @NameInMap("filter_group")
    public String filterGroup;

    @NameInMap("referer")
    public String referer;

    // share_name
    @NameInMap("share_name")
    public String shareName;

    // share_pwd
    @NameInMap("share_pwd")
    public String sharePwd;

    // user_id, only admin or aksk can set
    @NameInMap("user_id")
    public String userId;

    // view_id
    @NameInMap("view_id")
    public String viewId;

    public static CreateShareLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateShareLinkRequest self = new CreateShareLinkRequest();
        return TeaModel.build(map, self);
    }

    public CreateShareLinkRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CreateShareLinkRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public CreateShareLinkRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public CreateShareLinkRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateShareLinkRequest setDriveFileList(java.util.List<ShareFile> driveFileList) {
        this.driveFileList = driveFileList;
        return this;
    }
    public java.util.List<ShareFile> getDriveFileList() {
        return this.driveFileList;
    }

    public CreateShareLinkRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CreateShareLinkRequest setEnableFileChangedNotify(Boolean enableFileChangedNotify) {
        this.enableFileChangedNotify = enableFileChangedNotify;
        return this;
    }
    public Boolean getEnableFileChangedNotify() {
        return this.enableFileChangedNotify;
    }

    public CreateShareLinkRequest setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public CreateShareLinkRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public CreateShareLinkRequest setFileIdList(java.util.List<String> fileIdList) {
        this.fileIdList = fileIdList;
        return this;
    }
    public java.util.List<String> getFileIdList() {
        return this.fileIdList;
    }

    public CreateShareLinkRequest setFilePathList(java.util.List<String> filePathList) {
        this.filePathList = filePathList;
        return this;
    }
    public java.util.List<String> getFilePathList() {
        return this.filePathList;
    }

    public CreateShareLinkRequest setFilterGroup(String filterGroup) {
        this.filterGroup = filterGroup;
        return this;
    }
    public String getFilterGroup() {
        return this.filterGroup;
    }

    public CreateShareLinkRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public CreateShareLinkRequest setShareName(String shareName) {
        this.shareName = shareName;
        return this;
    }
    public String getShareName() {
        return this.shareName;
    }

    public CreateShareLinkRequest setSharePwd(String sharePwd) {
        this.sharePwd = sharePwd;
        return this;
    }
    public String getSharePwd() {
        return this.sharePwd;
    }

    public CreateShareLinkRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public CreateShareLinkRequest setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
