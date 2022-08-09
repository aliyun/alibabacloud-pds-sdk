// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 更新版本元数据
 */
public class UpdateRevisionRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // keep_forever
    // type: boolean
    @NameInMap("keep_forever")
    public Boolean keepForever;

    @NameInMap("referer")
    public String referer;

    // revision_description
    // type: string
    @NameInMap("revision_description")
    @Validation(maxLength = 1024)
    public String revisionDescription;

    // revision_id
    @NameInMap("revision_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String revisionId;

    @NameInMap("sign_token")
    public String signToken;

    public static UpdateRevisionRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateRevisionRequest self = new UpdateRevisionRequest();
        return TeaModel.build(map, self);
    }

    public UpdateRevisionRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateRevisionRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UpdateRevisionRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public UpdateRevisionRequest setKeepForever(Boolean keepForever) {
        this.keepForever = keepForever;
        return this;
    }
    public Boolean getKeepForever() {
        return this.keepForever;
    }

    public UpdateRevisionRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public UpdateRevisionRequest setRevisionDescription(String revisionDescription) {
        this.revisionDescription = revisionDescription;
        return this;
    }
    public String getRevisionDescription() {
        return this.revisionDescription;
    }

    public UpdateRevisionRequest setRevisionId(String revisionId) {
        this.revisionId = revisionId;
        return this;
    }
    public String getRevisionId() {
        return this.revisionId;
    }

    public UpdateRevisionRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

}
