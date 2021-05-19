// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 获取文件安全地址的请求body
 */
public class HostingGetSecureUrlRequest extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // expire_sec 单位秒
    @NameInMap("expire_sec")
    public Long expireSec;

    // file_path
    @NameInMap("file_path")
    @Validation(required = true, maxLength = 1000, minLength = 1)
    public String filePath;

    // secure_ip
    @NameInMap("secure_ip")
    public String secureIp;

    // share_id
    @NameInMap("share_id")
    @Validation(pattern = "[0-9a-zA-Z-]+")
    public String shareId;

    public static HostingGetSecureUrlRequest build(java.util.Map<String, ?> map) throws Exception {
        HostingGetSecureUrlRequest self = new HostingGetSecureUrlRequest();
        return TeaModel.build(map, self);
    }

    public HostingGetSecureUrlRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public HostingGetSecureUrlRequest setExpireSec(Long expireSec) {
        this.expireSec = expireSec;
        return this;
    }
    public Long getExpireSec() {
        return this.expireSec;
    }

    public HostingGetSecureUrlRequest setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public HostingGetSecureUrlRequest setSecureIp(String secureIp) {
        this.secureIp = secureIp;
        return this;
    }
    public String getSecureIp() {
        return this.secureIp;
    }

    public HostingGetSecureUrlRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
