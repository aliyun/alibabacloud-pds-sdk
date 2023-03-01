// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class FpRef extends TeaModel {
    /**
     * <p>domain_id</p>
     */
    @NameInMap("domain_id")
    public String domainId;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    public String driveId;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    public String fileId;

    /**
     * <p>file_revision_id</p>
     */
    @NameInMap("file_revision_id")
    public String fileRevisionId;

    public static FpRef build(java.util.Map<String, ?> map) throws Exception {
        FpRef self = new FpRef();
        return TeaModel.build(map, self);
    }

    public FpRef setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public FpRef setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public FpRef setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public FpRef setFileRevisionId(String fileRevisionId) {
        this.fileRevisionId = fileRevisionId;
        return this;
    }
    public String getFileRevisionId() {
        return this.fileRevisionId;
    }

}
