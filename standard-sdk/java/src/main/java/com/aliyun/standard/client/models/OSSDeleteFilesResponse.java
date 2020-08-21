// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 批量删除文件 response
 */
public class OSSDeleteFilesResponse extends TeaModel {
    // deleted_file_id_list
    @NameInMap("deleted_file_id_list")
    public java.util.List<String> deletedFileIdList;

    // domain_id
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String domainId;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // share_id
    @NameInMap("share_id")
    @Validation(pattern = "[0-9]+")
    public String shareId;

    public static OSSDeleteFilesResponse build(java.util.Map<String, ?> map) throws Exception {
        OSSDeleteFilesResponse self = new OSSDeleteFilesResponse();
        return TeaModel.build(map, self);
    }

    public OSSDeleteFilesResponse setDeletedFileIdList(java.util.List<String> deletedFileIdList) {
        this.deletedFileIdList = deletedFileIdList;
        return this;
    }
    public java.util.List<String> getDeletedFileIdList() {
        return this.deletedFileIdList;
    }

    public OSSDeleteFilesResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public OSSDeleteFilesResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public OSSDeleteFilesResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
