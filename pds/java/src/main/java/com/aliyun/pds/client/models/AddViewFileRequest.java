// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * add file to view
 */
public class AddViewFileRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>category</p>
     */
    @NameInMap("category")
    @Validation(required = true)
    public String category;

    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("fields")
    public java.util.Map<String, ?> fields;

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

    public static AddViewFileRequest build(java.util.Map<String, ?> map) throws Exception {
        AddViewFileRequest self = new AddViewFileRequest();
        return TeaModel.build(map, self);
    }

    public AddViewFileRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public AddViewFileRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public AddViewFileRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public AddViewFileRequest setFields(java.util.Map<String, ?> fields) {
        this.fields = fields;
        return this;
    }
    public java.util.Map<String, ?> getFields() {
        return this.fields;
    }

    public AddViewFileRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public AddViewFileRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public AddViewFileRequest setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
