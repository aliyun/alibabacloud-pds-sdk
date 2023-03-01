// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * get file from view
 */
public class GetViewFileRequest extends TeaModel {
    /**
     * <p>category</p>
     */
    @NameInMap("category")
    @Validation(required = true)
    public String category;

    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("file_id")
    public String fileId;

    /**
     * <p>user_id</p>
     */
    @NameInMap("user_id")
    public String userId;

    /**
     * <p>view_id</p>
     */
    @NameInMap("view_id")
    @Validation(required = true)
    public String viewId;

    public static GetViewFileRequest build(java.util.Map<String, ?> map) throws Exception {
        GetViewFileRequest self = new GetViewFileRequest();
        return TeaModel.build(map, self);
    }

    public GetViewFileRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public GetViewFileRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetViewFileRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public GetViewFileRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public GetViewFileRequest setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
