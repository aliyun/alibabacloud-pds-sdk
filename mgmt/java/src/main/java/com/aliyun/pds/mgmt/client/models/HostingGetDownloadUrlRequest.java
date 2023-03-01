// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 获取文件下载地址的请求body
 */
public class HostingGetDownloadUrlRequest extends TeaModel {
    /**
     * <p>addition_data</p>
     */
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>expire_sec</p>
     */
    @NameInMap("expire_sec")
    @Validation(maximum = 115200, minimum = 10)
    public Long expireSec;

    /**
     * <p>file_name</p>
     */
    @NameInMap("file_name")
    public String fileName;

    /**
     * <p>file_path</p>
     */
    @NameInMap("file_path")
    @Validation(required = true, maxLength = 1000, minLength = 1)
    public String filePath;

    @NameInMap("referer")
    public String referer;

    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    @Validation(pattern = "[0-9a-zA-Z-]+")
    public String shareId;

    @NameInMap("sign_token")
    public String signToken;

    public static HostingGetDownloadUrlRequest build(java.util.Map<String, ?> map) throws Exception {
        HostingGetDownloadUrlRequest self = new HostingGetDownloadUrlRequest();
        return TeaModel.build(map, self);
    }

    public HostingGetDownloadUrlRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public HostingGetDownloadUrlRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public HostingGetDownloadUrlRequest setExpireSec(Long expireSec) {
        this.expireSec = expireSec;
        return this;
    }
    public Long getExpireSec() {
        return this.expireSec;
    }

    public HostingGetDownloadUrlRequest setFileName(String fileName) {
        this.fileName = fileName;
        return this;
    }
    public String getFileName() {
        return this.fileName;
    }

    public HostingGetDownloadUrlRequest setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public HostingGetDownloadUrlRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public HostingGetDownloadUrlRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public HostingGetDownloadUrlRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

}
