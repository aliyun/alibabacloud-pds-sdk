// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 更新文件元数据
 */
public class UpdateFileMetaRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // check_name_mode
    @NameInMap("check_name_mode")
    public String checkNameMode;

    @NameInMap("custom_index_key")
    public String customIndexKey;

    // description
    // type: string
    @NameInMap("description")
    @Validation(maxLength = 1024)
    public String description;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    @NameInMap("encrypt_mode")
    public String encryptMode;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    @NameInMap("file_id_path")
    public String fileIdPath;

    // hidden
    // type: boolean
    @NameInMap("hidden")
    public Boolean hidden;

    // labels
    @NameInMap("labels")
    public java.util.List<String> labels;

    @NameInMap("meta")
    public String meta;

    // name
    @NameInMap("name")
    @Validation(maxLength = 1024, minLength = 1)
    public String name;

    @NameInMap("referer")
    public String referer;

    @NameInMap("share_id")
    public String shareId;

    @NameInMap("sign_token")
    public String signToken;

    // starred
    // type: boolean
    @NameInMap("starred")
    public Boolean starred;

    // user_meta
    @NameInMap("user_meta")
    public String userMeta;

    public static UpdateFileMetaRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateFileMetaRequest self = new UpdateFileMetaRequest();
        return TeaModel.build(map, self);
    }

    public UpdateFileMetaRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateFileMetaRequest setCheckNameMode(String checkNameMode) {
        this.checkNameMode = checkNameMode;
        return this;
    }
    public String getCheckNameMode() {
        return this.checkNameMode;
    }

    public UpdateFileMetaRequest setCustomIndexKey(String customIndexKey) {
        this.customIndexKey = customIndexKey;
        return this;
    }
    public String getCustomIndexKey() {
        return this.customIndexKey;
    }

    public UpdateFileMetaRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateFileMetaRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UpdateFileMetaRequest setEncryptMode(String encryptMode) {
        this.encryptMode = encryptMode;
        return this;
    }
    public String getEncryptMode() {
        return this.encryptMode;
    }

    public UpdateFileMetaRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public UpdateFileMetaRequest setFileIdPath(String fileIdPath) {
        this.fileIdPath = fileIdPath;
        return this;
    }
    public String getFileIdPath() {
        return this.fileIdPath;
    }

    public UpdateFileMetaRequest setHidden(Boolean hidden) {
        this.hidden = hidden;
        return this;
    }
    public Boolean getHidden() {
        return this.hidden;
    }

    public UpdateFileMetaRequest setLabels(java.util.List<String> labels) {
        this.labels = labels;
        return this;
    }
    public java.util.List<String> getLabels() {
        return this.labels;
    }

    public UpdateFileMetaRequest setMeta(String meta) {
        this.meta = meta;
        return this;
    }
    public String getMeta() {
        return this.meta;
    }

    public UpdateFileMetaRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public UpdateFileMetaRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public UpdateFileMetaRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public UpdateFileMetaRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

    public UpdateFileMetaRequest setStarred(Boolean starred) {
        this.starred = starred;
        return this;
    }
    public Boolean getStarred() {
        return this.starred;
    }

    public UpdateFileMetaRequest setUserMeta(String userMeta) {
        this.userMeta = userMeta;
        return this;
    }
    public String getUserMeta() {
        return this.userMeta;
    }

}
