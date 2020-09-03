// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * create_share_link request
 */
public class CreateShareLinkRequest extends TeaModel {
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

    // share_pwd
    @NameInMap("share_pwd")
    public String sharePwd;

    public static CreateShareLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateShareLinkRequest self = new CreateShareLinkRequest();
        return TeaModel.build(map, self);
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

    public CreateShareLinkRequest setSharePwd(String sharePwd) {
        this.sharePwd = sharePwd;
        return this;
    }
    public String getSharePwd() {
        return this.sharePwd;
    }

}
