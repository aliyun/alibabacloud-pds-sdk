// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Update view request
 */
public class UpdateViewRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // category
    @NameInMap("category")
    @Validation(required = true)
    public String category;

    // description
    @NameInMap("description")
    public String description;

    // ex_fields_info
    @NameInMap("ex_fields_info")
    public java.util.Map<String, ?> exFieldsInfo;

    // description
    @NameInMap("file_count")
    public Long fileCount;

    // name
    @NameInMap("name")
    public String name;

    // user_id
    @NameInMap("user_id")
    public String userId;

    // view_id
    @NameInMap("view_id")
    @Validation(required = true)
    public String viewId;

    public static UpdateViewRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateViewRequest self = new UpdateViewRequest();
        return TeaModel.build(map, self);
    }

    public UpdateViewRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateViewRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public UpdateViewRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateViewRequest setExFieldsInfo(java.util.Map<String, ?> exFieldsInfo) {
        this.exFieldsInfo = exFieldsInfo;
        return this;
    }
    public java.util.Map<String, ?> getExFieldsInfo() {
        return this.exFieldsInfo;
    }

    public UpdateViewRequest setFileCount(Long fileCount) {
        this.fileCount = fileCount;
        return this;
    }
    public Long getFileCount() {
        return this.fileCount;
    }

    public UpdateViewRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public UpdateViewRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public UpdateViewRequest setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
