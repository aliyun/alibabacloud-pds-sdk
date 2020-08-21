// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * Search image address groups request
 */
public class SearchImageAddressGroupsRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 查询的地点级别
    @NameInMap("address_level")
    public String addressLevel;

    // 查询的地点数组
    @NameInMap("address_names")
    public java.util.List<String> addressNames;

    // br_geo_point
    @NameInMap("br_geo_point")
    public String brGeoPoint;

    // Drive ID
    @NameInMap("drive_id")
    @Validation(required = true)
    public String driveId;

    // image_thumbnail_process
type:string
    @NameInMap("image_thumbnail_process")
    public String imageThumbnailProcess;

    // tl_geo_point
    @NameInMap("tl_geo_point")
    public String tlGeoPoint;

    public static SearchImageAddressGroupsRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchImageAddressGroupsRequest self = new SearchImageAddressGroupsRequest();
        return TeaModel.build(map, self);
    }

    public SearchImageAddressGroupsRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchImageAddressGroupsRequest setAddressLevel(String addressLevel) {
        this.addressLevel = addressLevel;
        return this;
    }
    public String getAddressLevel() {
        return this.addressLevel;
    }

    public SearchImageAddressGroupsRequest setAddressNames(java.util.List<String> addressNames) {
        this.addressNames = addressNames;
        return this;
    }
    public java.util.List<String> getAddressNames() {
        return this.addressNames;
    }

    public SearchImageAddressGroupsRequest setBrGeoPoint(String brGeoPoint) {
        this.brGeoPoint = brGeoPoint;
        return this;
    }
    public String getBrGeoPoint() {
        return this.brGeoPoint;
    }

    public SearchImageAddressGroupsRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public SearchImageAddressGroupsRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public SearchImageAddressGroupsRequest setTlGeoPoint(String tlGeoPoint) {
        this.tlGeoPoint = tlGeoPoint;
        return this;
    }
    public String getTlGeoPoint() {
        return this.tlGeoPoint;
    }

}
