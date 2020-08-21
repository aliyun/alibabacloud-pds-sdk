// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取文件安全地址的请求body
 */
public class OSSGetSecureUrlRequest extends TeaModel {
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

    public static OSSGetSecureUrlRequest build(java.util.Map<String, ?> map) throws Exception {
        OSSGetSecureUrlRequest self = new OSSGetSecureUrlRequest();
        return TeaModel.build(map, self);
    }

    public OSSGetSecureUrlRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public OSSGetSecureUrlRequest setExpireSec(Long expireSec) {
        this.expireSec = expireSec;
        return this;
    }
    public Long getExpireSec() {
        return this.expireSec;
    }

    public OSSGetSecureUrlRequest setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public OSSGetSecureUrlRequest setSecureIp(String secureIp) {
        this.secureIp = secureIp;
        return this;
    }
    public String getSecureIp() {
        return this.secureIp;
    }

    public OSSGetSecureUrlRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
