// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取视频分辨率列表
 */
public class HostingVideoDefinitionRequest extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_path
    @NameInMap("file_path")
    @Validation(required = true, maxLength = 1000, minLength = 1)
    public String filePath;

    // protection_scheme
    @NameInMap("protection_scheme")
    public String protectionScheme;

    // share_id
    @NameInMap("share_id")
    @Validation(pattern = "[0-9a-zA-Z-]+")
    public String shareId;

    public static HostingVideoDefinitionRequest build(java.util.Map<String, ?> map) throws Exception {
        HostingVideoDefinitionRequest self = new HostingVideoDefinitionRequest();
        return TeaModel.build(map, self);
    }

    public HostingVideoDefinitionRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public HostingVideoDefinitionRequest setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public HostingVideoDefinitionRequest setProtectionScheme(String protectionScheme) {
        this.protectionScheme = protectionScheme;
        return this;
    }
    public String getProtectionScheme() {
        return this.protectionScheme;
    }

    public HostingVideoDefinitionRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
