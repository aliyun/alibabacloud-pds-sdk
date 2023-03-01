// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Search image address groups request
 */
public class SearchImageAddressGroupsRequest extends TeaModel {
    /**
     * <p>查询的地点级别</p>
     */
    @NameInMap("address_level")
    public String addressLevel;

    /**
     * <p>查询的地点数组</p>
     */
    @NameInMap("address_names")
    public java.util.List<String> addressNames;

    /**
     * <p>br_geo_point</p>
     */
    @NameInMap("br_geo_point")
    public String brGeoPoint;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>image_thumbnail_process</p>
     */
    @NameInMap("image_thumbnail_process")
    public String imageThumbnailProcess;

    /**
     * <p>tl_geo_point</p>
     */
    @NameInMap("tl_geo_point")
    public String tlGeoPoint;

    /**
     * <p>video_thumbnail_process</p>
     */
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static SearchImageAddressGroupsRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchImageAddressGroupsRequest self = new SearchImageAddressGroupsRequest();
        return TeaModel.build(map, self);
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

    public SearchImageAddressGroupsRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
