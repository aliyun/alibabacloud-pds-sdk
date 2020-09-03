// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 批量删除文件 response
 */
public class HostingDeleteFilesResponse extends TeaModel {
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

    public static HostingDeleteFilesResponse build(java.util.Map<String, ?> map) throws Exception {
        HostingDeleteFilesResponse self = new HostingDeleteFilesResponse();
        return TeaModel.build(map, self);
    }

    public HostingDeleteFilesResponse setDeletedFileIdList(java.util.List<String> deletedFileIdList) {
        this.deletedFileIdList = deletedFileIdList;
        return this;
    }
    public java.util.List<String> getDeletedFileIdList() {
        return this.deletedFileIdList;
    }

    public HostingDeleteFilesResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public HostingDeleteFilesResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public HostingDeleteFilesResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
