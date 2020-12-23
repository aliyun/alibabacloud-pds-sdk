// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * create_share_link request
 */
public class CreateShareLinkRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // expiration
    @NameInMap("expiration")
    @Validation(required = true)
    public String expiration;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true)
    public String fileId;

    // file_id_list
    @NameInMap("file_id_list")
    @Validation(required = true)
    public java.util.List<String> fileIdList;

    // file_path_list
    @NameInMap("file_path_list")
    @Validation(required = true)
    public java.util.List<String> filePathList;

    // share_pwd
    @NameInMap("share_pwd")
    public String sharePwd;

    public static CreateShareLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateShareLinkRequest self = new CreateShareLinkRequest();
        return TeaModel.build(map, self);
    }

    public CreateShareLinkRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateShareLinkRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
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

    public CreateShareLinkRequest setSharePwd(String sharePwd) {
        this.sharePwd = sharePwd;
        return this;
    }
    public String getSharePwd() {
        return this.sharePwd;
    }

}
