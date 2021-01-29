// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 搜索文件元数据
 */
public class SearchFileRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

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
    public Integer limit;

    // location
    @NameInMap("location")
    public String location;

    // Marker
    @NameInMap("marker")
    public String marker;

    // order_by
    @NameInMap("order_by")
    public String orderBy;

    // query
    @NameInMap("query")
    @Validation(maxLength = 4096)
    public String query;

    // referer
    @NameInMap("referer")
    public String referer;

    // return_total_count 是否返回查询总数
    @NameInMap("return_total_count")
    public Boolean returnTotalCount;

    // sign_token
    @NameInMap("sign_token")
    public String signToken;

    // url_expire_sec
    @NameInMap("url_expire_sec")
    public Long urlExpireSec;

    // video_thumbnail_process
    // type:string
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static SearchFileRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchFileRequest self = new SearchFileRequest();
        return TeaModel.build(map, self);
    }

    public SearchFileRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchFileRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public SearchFileRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public SearchFileRequest setImageCroppingAspectRatios(java.util.List<String> imageCroppingAspectRatios) {
        this.imageCroppingAspectRatios = imageCroppingAspectRatios;
        return this;
    }
    public java.util.List<String> getImageCroppingAspectRatios() {
        return this.imageCroppingAspectRatios;
    }

    public SearchFileRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public SearchFileRequest setImageUrlProcess(String imageUrlProcess) {
        this.imageUrlProcess = imageUrlProcess;
        return this;
    }
    public String getImageUrlProcess() {
        return this.imageUrlProcess;
    }

    public SearchFileRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public SearchFileRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public SearchFileRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public SearchFileRequest setOrderBy(String orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public String getOrderBy() {
        return this.orderBy;
    }

    public SearchFileRequest setQuery(String query) {
        this.query = query;
        return this;
    }
    public String getQuery() {
        return this.query;
    }

    public SearchFileRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public SearchFileRequest setReturnTotalCount(Boolean returnTotalCount) {
        this.returnTotalCount = returnTotalCount;
        return this;
    }
    public Boolean getReturnTotalCount() {
        return this.returnTotalCount;
    }

    public SearchFileRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

    public SearchFileRequest setUrlExpireSec(Long urlExpireSec) {
        this.urlExpireSec = urlExpireSec;
        return this;
    }
    public Long getUrlExpireSec() {
        return this.urlExpireSec;
    }

    public SearchFileRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
