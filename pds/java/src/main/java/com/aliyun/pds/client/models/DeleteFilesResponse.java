// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 批量删除文件 response
 */
public class DeleteFilesResponse extends TeaModel {
    /**
     * <p>deleted_file_id_list</p>
     */
    @NameInMap("deleted_file_id_list")
    public java.util.List<String> deletedFileIdList;

    /**
     * <p>domain_id</p>
     */
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String domainId;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    public static DeleteFilesResponse build(java.util.Map<String, ?> map) throws Exception {
        DeleteFilesResponse self = new DeleteFilesResponse();
        return TeaModel.build(map, self);
    }

    public DeleteFilesResponse setDeletedFileIdList(java.util.List<String> deletedFileIdList) {
        this.deletedFileIdList = deletedFileIdList;
        return this;
    }
    public java.util.List<String> getDeletedFileIdList() {
        return this.deletedFileIdList;
    }

    public DeleteFilesResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public DeleteFilesResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
