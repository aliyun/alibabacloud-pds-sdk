// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 获取视频的m3u8文件
 */
public class HostingVideoM3U8Request extends TeaModel {
    // definition
    @NameInMap("definition")
    public String definition;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // expire_sec
    @NameInMap("expire_sec")
    @Validation(maximum = 86400, minimum = 60)
    public Long expireSec;

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

    // sign_token
    @NameInMap("sign_token")
    @Validation(required = true)
    public String signToken;

    public static HostingVideoM3U8Request build(java.util.Map<String, ?> map) throws Exception {
        HostingVideoM3U8Request self = new HostingVideoM3U8Request();
        return TeaModel.build(map, self);
    }

    public HostingVideoM3U8Request setDefinition(String definition) {
        this.definition = definition;
        return this;
    }
    public String getDefinition() {
        return this.definition;
    }

    public HostingVideoM3U8Request setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public HostingVideoM3U8Request setExpireSec(Long expireSec) {
        this.expireSec = expireSec;
        return this;
    }
    public Long getExpireSec() {
        return this.expireSec;
    }

    public HostingVideoM3U8Request setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public HostingVideoM3U8Request setProtectionScheme(String protectionScheme) {
        this.protectionScheme = protectionScheme;
        return this;
    }
    public String getProtectionScheme() {
        return this.protectionScheme;
    }

    public HostingVideoM3U8Request setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public HostingVideoM3U8Request setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

}
