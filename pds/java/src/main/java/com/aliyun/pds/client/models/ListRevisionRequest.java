// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 列举版本
 */
public class ListRevisionRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // fields
    @NameInMap("fields")
    public String fields;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 4)
    public String fileId;

    @NameInMap("image_cropping_aspect_ratios")
    public java.util.List<String> imageCroppingAspectRatios;

    // image_thumbnail_process
    @NameInMap("image_thumbnail_process")
    public String imageThumbnailProcess;

    // image_url_process
    @NameInMap("image_url_process")
    public String imageUrlProcess;

    // limit
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Long limit;

    // location
    @NameInMap("location")
    public String location;

    // marker
    @NameInMap("marker")
    public String marker;

    // office_thumbnail_process
    @NameInMap("office_thumbnail_process")
    public String officeThumbnailProcess;

    // query
    @NameInMap("query")
    public String query;

    @NameInMap("referer")
    public String referer;

    @NameInMap("sign_token")
    public String signToken;

    // url_expire_sec
    @NameInMap("url_expire_sec")
    @Validation(maximum = 14400, minimum = 10)
    public Long urlExpireSec;

    // video_thumbnail_process
    // type:string
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static ListRevisionRequest build(java.util.Map<String, ?> map) throws Exception {
        ListRevisionRequest self = new ListRevisionRequest();
        return TeaModel.build(map, self);
    }

    public ListRevisionRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ListRevisionRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public ListRevisionRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ListRevisionRequest setFields(String fields) {
        this.fields = fields;
        return this;
    }
    public String getFields() {
        return this.fields;
    }

    public ListRevisionRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public ListRevisionRequest setImageCroppingAspectRatios(java.util.List<String> imageCroppingAspectRatios) {
        this.imageCroppingAspectRatios = imageCroppingAspectRatios;
        return this;
    }
    public java.util.List<String> getImageCroppingAspectRatios() {
        return this.imageCroppingAspectRatios;
    }

    public ListRevisionRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public ListRevisionRequest setImageUrlProcess(String imageUrlProcess) {
        this.imageUrlProcess = imageUrlProcess;
        return this;
    }
    public String getImageUrlProcess() {
        return this.imageUrlProcess;
    }

    public ListRevisionRequest setLimit(Long limit) {
        this.limit = limit;
        return this;
    }
    public Long getLimit() {
        return this.limit;
    }

    public ListRevisionRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public ListRevisionRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListRevisionRequest setOfficeThumbnailProcess(String officeThumbnailProcess) {
        this.officeThumbnailProcess = officeThumbnailProcess;
        return this;
    }
    public String getOfficeThumbnailProcess() {
        return this.officeThumbnailProcess;
    }

    public ListRevisionRequest setQuery(String query) {
        this.query = query;
        return this;
    }
    public String getQuery() {
        return this.query;
    }

    public ListRevisionRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public ListRevisionRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

    public ListRevisionRequest setUrlExpireSec(Long urlExpireSec) {
        this.urlExpireSec = urlExpireSec;
        return this;
    }
    public Long getUrlExpireSec() {
        return this.urlExpireSec;
    }

    public ListRevisionRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
