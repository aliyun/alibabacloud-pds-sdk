// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 列举回收站
 */
public class ListFileInRecycleBinRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // starred
    @NameInMap("Starred")
    public Boolean Starred;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // all
    @NameInMap("all")
    public Boolean all;

    // category
    @NameInMap("category")
    public String category;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // fields
    @NameInMap("fields")
    public String fields;

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
    @Validation(maximum = 200)
    public Long limit;

    // marker
    @NameInMap("marker")
    public String marker;

    // office_thumbnail_process
    @NameInMap("office_thumbnail_process")
    public String officeThumbnailProcess;

    // order_by
    @NameInMap("order_by")
    public String orderBy;

    // order_direction
    @NameInMap("order_direction")
    public String orderDirection;

    // ParentFileID
    @NameInMap("parent_file_id")
    @Validation(pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 4)
    public String parentFileId;

    @NameInMap("referer")
    public String referer;

    // share_id, either share_id or drive_id is required
    @NameInMap("share_id")
    public String shareId;

    @NameInMap("sign_token")
    public String signToken;

    // status
    @NameInMap("status")
    public String status;

    @NameInMap("thumbnail_processes")
    public java.util.Map<String, ?> thumbnailProcesses;

    // type
    @NameInMap("type")
    public String type;

    // url_expire_sec
    @NameInMap("url_expire_sec")
    @Validation(maximum = 14400, minimum = 10)
    public Long urlExpireSec;

    // video_thumbnail_process
    // type:string
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static ListFileInRecycleBinRequest build(java.util.Map<String, ?> map) throws Exception {
        ListFileInRecycleBinRequest self = new ListFileInRecycleBinRequest();
        return TeaModel.build(map, self);
    }

    public ListFileInRecycleBinRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ListFileInRecycleBinRequest setStarred(Boolean Starred) {
        this.Starred = Starred;
        return this;
    }
    public Boolean getStarred() {
        return this.Starred;
    }

    public ListFileInRecycleBinRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public ListFileInRecycleBinRequest setAll(Boolean all) {
        this.all = all;
        return this;
    }
    public Boolean getAll() {
        return this.all;
    }

    public ListFileInRecycleBinRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public ListFileInRecycleBinRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ListFileInRecycleBinRequest setFields(String fields) {
        this.fields = fields;
        return this;
    }
    public String getFields() {
        return this.fields;
    }

    public ListFileInRecycleBinRequest setImageCroppingAspectRatios(java.util.List<String> imageCroppingAspectRatios) {
        this.imageCroppingAspectRatios = imageCroppingAspectRatios;
        return this;
    }
    public java.util.List<String> getImageCroppingAspectRatios() {
        return this.imageCroppingAspectRatios;
    }

    public ListFileInRecycleBinRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public ListFileInRecycleBinRequest setImageUrlProcess(String imageUrlProcess) {
        this.imageUrlProcess = imageUrlProcess;
        return this;
    }
    public String getImageUrlProcess() {
        return this.imageUrlProcess;
    }

    public ListFileInRecycleBinRequest setLimit(Long limit) {
        this.limit = limit;
        return this;
    }
    public Long getLimit() {
        return this.limit;
    }

    public ListFileInRecycleBinRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListFileInRecycleBinRequest setOfficeThumbnailProcess(String officeThumbnailProcess) {
        this.officeThumbnailProcess = officeThumbnailProcess;
        return this;
    }
    public String getOfficeThumbnailProcess() {
        return this.officeThumbnailProcess;
    }

    public ListFileInRecycleBinRequest setOrderBy(String orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public String getOrderBy() {
        return this.orderBy;
    }

    public ListFileInRecycleBinRequest setOrderDirection(String orderDirection) {
        this.orderDirection = orderDirection;
        return this;
    }
    public String getOrderDirection() {
        return this.orderDirection;
    }

    public ListFileInRecycleBinRequest setParentFileId(String parentFileId) {
        this.parentFileId = parentFileId;
        return this;
    }
    public String getParentFileId() {
        return this.parentFileId;
    }

    public ListFileInRecycleBinRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public ListFileInRecycleBinRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public ListFileInRecycleBinRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

    public ListFileInRecycleBinRequest setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public ListFileInRecycleBinRequest setThumbnailProcesses(java.util.Map<String, ?> thumbnailProcesses) {
        this.thumbnailProcesses = thumbnailProcesses;
        return this;
    }
    public java.util.Map<String, ?> getThumbnailProcesses() {
        return this.thumbnailProcesses;
    }

    public ListFileInRecycleBinRequest setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public ListFileInRecycleBinRequest setUrlExpireSec(Long urlExpireSec) {
        this.urlExpireSec = urlExpireSec;
        return this;
    }
    public Long getUrlExpireSec() {
        return this.urlExpireSec;
    }

    public ListFileInRecycleBinRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
