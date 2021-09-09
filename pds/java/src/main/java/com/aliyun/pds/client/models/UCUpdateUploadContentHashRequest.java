// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * UCUpdateUploadContentHashRequest update upload info
 */
public class UCUpdateUploadContentHashRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // content_hash
    @NameInMap("content_hash")
    public String contentHash;

    // content_hash_name
    @NameInMap("content_hash_name")
    public String contentHashName;

    // content_md5
    @NameInMap("content_md5")
    public String contentMd5;

    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    public String fileId;

    // overwrite
    @NameInMap("overwrite")
    public Boolean overwrite;

    // size
    @NameInMap("size")
    public Long size;

    // upload_id
    @NameInMap("upload_id")
    public String uploadId;

    public static UCUpdateUploadContentHashRequest build(java.util.Map<String, ?> map) throws Exception {
        UCUpdateUploadContentHashRequest self = new UCUpdateUploadContentHashRequest();
        return TeaModel.build(map, self);
    }

    public UCUpdateUploadContentHashRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UCUpdateUploadContentHashRequest setContentHash(String contentHash) {
        this.contentHash = contentHash;
        return this;
    }
    public String getContentHash() {
        return this.contentHash;
    }

    public UCUpdateUploadContentHashRequest setContentHashName(String contentHashName) {
        this.contentHashName = contentHashName;
        return this;
    }
    public String getContentHashName() {
        return this.contentHashName;
    }

    public UCUpdateUploadContentHashRequest setContentMd5(String contentMd5) {
        this.contentMd5 = contentMd5;
        return this;
    }
    public String getContentMd5() {
        return this.contentMd5;
    }

    public UCUpdateUploadContentHashRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UCUpdateUploadContentHashRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public UCUpdateUploadContentHashRequest setOverwrite(Boolean overwrite) {
        this.overwrite = overwrite;
        return this;
    }
    public Boolean getOverwrite() {
        return this.overwrite;
    }

    public UCUpdateUploadContentHashRequest setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public UCUpdateUploadContentHashRequest setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

}
