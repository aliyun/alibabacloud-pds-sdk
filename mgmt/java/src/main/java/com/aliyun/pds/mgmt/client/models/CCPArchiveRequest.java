// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CCPArchiveRequest extends TeaModel {
    /**
     * <p>格式类型，如果是uc，使用特殊格式</p>
     */
    @NameInMap("Format")
    public String Format;

    @NameInMap("RequestID")
    public String RequestID;

    @NameInMap("archive_type")
    public String archiveType;

    @NameInMap("domain_id")
    public String domainId;

    /**
     * <p>TODO 增加对ShareID的支持</p>
     */
    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("file_id")
    public String fileId;

    @NameInMap("password")
    public String password;

    public static CCPArchiveRequest build(java.util.Map<String, ?> map) throws Exception {
        CCPArchiveRequest self = new CCPArchiveRequest();
        return TeaModel.build(map, self);
    }

    public CCPArchiveRequest setFormat(String Format) {
        this.Format = Format;
        return this;
    }
    public String getFormat() {
        return this.Format;
    }

    public CCPArchiveRequest setRequestID(String RequestID) {
        this.RequestID = RequestID;
        return this;
    }
    public String getRequestID() {
        return this.RequestID;
    }

    public CCPArchiveRequest setArchiveType(String archiveType) {
        this.archiveType = archiveType;
        return this;
    }
    public String getArchiveType() {
        return this.archiveType;
    }

    public CCPArchiveRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public CCPArchiveRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CCPArchiveRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public CCPArchiveRequest setPassword(String password) {
        this.password = password;
        return this;
    }
    public String getPassword() {
        return this.password;
    }

}
