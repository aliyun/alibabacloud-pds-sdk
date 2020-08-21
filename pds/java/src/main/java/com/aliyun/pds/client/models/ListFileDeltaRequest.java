// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取增量文件操作记录
 */
public class ListFileDeltaRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // cursor 游标
    @NameInMap("cursor")
    public String cursor;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // limit
    // default 100
    @NameInMap("limit")
    public Integer limit;

    public static ListFileDeltaRequest build(java.util.Map<String, ?> map) throws Exception {
        ListFileDeltaRequest self = new ListFileDeltaRequest();
        return TeaModel.build(map, self);
    }

    public ListFileDeltaRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListFileDeltaRequest setCursor(String cursor) {
        this.cursor = cursor;
        return this;
    }
    public String getCursor() {
        return this.cursor;
    }

    public ListFileDeltaRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ListFileDeltaRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

}
