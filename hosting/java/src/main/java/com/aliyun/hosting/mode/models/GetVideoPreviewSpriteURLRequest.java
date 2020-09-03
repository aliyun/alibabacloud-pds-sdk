// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 获取视频雪碧图地址的请求body
 */
public class GetVideoPreviewSpriteURLRequest extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // expire_sec
    @NameInMap("expire_sec")
    public Long expireSec;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    public static GetVideoPreviewSpriteURLRequest build(java.util.Map<String, ?> map) throws Exception {
        GetVideoPreviewSpriteURLRequest self = new GetVideoPreviewSpriteURLRequest();
        return TeaModel.build(map, self);
    }

    public GetVideoPreviewSpriteURLRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetVideoPreviewSpriteURLRequest setExpireSec(Long expireSec) {
        this.expireSec = expireSec;
        return this;
    }
    public Long getExpireSec() {
        return this.expireSec;
    }

    public GetVideoPreviewSpriteURLRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

}
