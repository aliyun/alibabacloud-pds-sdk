// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * list file view ids
 */
public class ListFileViewsRequest extends TeaModel {
    @NameInMap("category")
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

    public static ListFileViewsRequest build(java.util.Map<String, ?> map) throws Exception {
        ListFileViewsRequest self = new ListFileViewsRequest();
        return TeaModel.build(map, self);
    }

    public ListFileViewsRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public ListFileViewsRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ListFileViewsRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public ListFileViewsRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
