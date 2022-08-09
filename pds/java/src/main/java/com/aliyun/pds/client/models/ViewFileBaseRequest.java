// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class ViewFileBaseRequest extends TeaModel {
    // category
    @NameInMap("category")
    @Validation(required = true)
    public String category;

    @NameInMap("drive_id")
    public String driveId;

    // user_id
    @NameInMap("user_id")
    public String userId;

    // view_id
    @NameInMap("view_id")
    @Validation(required = true)
    public String viewId;

    public static ViewFileBaseRequest build(java.util.Map<String, ?> map) throws Exception {
        ViewFileBaseRequest self = new ViewFileBaseRequest();
        return TeaModel.build(map, self);
    }

    public ViewFileBaseRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public ViewFileBaseRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ViewFileBaseRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public ViewFileBaseRequest setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
