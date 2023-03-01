// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * search file request
 */
public class SearchFileFpRefsRequest extends TeaModel {
    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    @Validation(required = true)
    public String fileId;

    /**
     * <p>file_revision_id</p>
     */
    @NameInMap("file_revision_id")
    @Validation(required = true)
    public String fileRevisionId;

    /**
     * <p>marker</p>
     */
    @NameInMap("marker")
    public String marker;

    public static SearchFileFpRefsRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchFileFpRefsRequest self = new SearchFileFpRefsRequest();
        return TeaModel.build(map, self);
    }

    public SearchFileFpRefsRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public SearchFileFpRefsRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public SearchFileFpRefsRequest setFileRevisionId(String fileRevisionId) {
        this.fileRevisionId = fileRevisionId;
        return this;
    }
    public String getFileRevisionId() {
        return this.fileRevisionId;
    }

    public SearchFileFpRefsRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

}
