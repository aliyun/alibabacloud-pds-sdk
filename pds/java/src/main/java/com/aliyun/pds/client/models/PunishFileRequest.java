// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 处罚文件请求
 */
public class PunishFileRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("action_code")
    public String actionCode;

    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("file_id")
    public String fileId;

    @NameInMap("punish_reason")
    public String punishReason;

    public static PunishFileRequest build(java.util.Map<String, ?> map) throws Exception {
        PunishFileRequest self = new PunishFileRequest();
        return TeaModel.build(map, self);
    }

    public PunishFileRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public PunishFileRequest setActionCode(String actionCode) {
        this.actionCode = actionCode;
        return this;
    }
    public String getActionCode() {
        return this.actionCode;
    }

    public PunishFileRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public PunishFileRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public PunishFileRequest setPunishReason(String punishReason) {
        this.punishReason = punishReason;
        return this;
    }
    public String getPunishReason() {
        return this.punishReason;
    }

}
