// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * list share request
 */
public class ListShareRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // creator
    @NameInMap("creator")
    public String creator;

    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // limit
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Integer limit;

    // marker
    @NameInMap("marker")
    public String marker;

    // Owner
    @NameInMap("owner")
    public String owner;

    // owner_type
    @NameInMap("owner_type")
    public String ownerType;

    // share_file_path
    @NameInMap("share_file_path")
    public String shareFilePath;

    public static ListShareRequest build(java.util.Map<String, ?> map) throws Exception {
        ListShareRequest self = new ListShareRequest();
        return TeaModel.build(map, self);
    }

    public ListShareRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListShareRequest setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public ListShareRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ListShareRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListShareRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListShareRequest setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public ListShareRequest setOwnerType(String ownerType) {
        this.ownerType = ownerType;
        return this;
    }
    public String getOwnerType() {
        return this.ownerType;
    }

    public ListShareRequest setShareFilePath(String shareFilePath) {
        this.shareFilePath = shareFilePath;
        return this;
    }
    public String getShareFilePath() {
        return this.shareFilePath;
    }

}
