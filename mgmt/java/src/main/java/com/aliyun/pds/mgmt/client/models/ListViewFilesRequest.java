// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * list view file
 */
public class ListViewFilesRequest extends TeaModel {
    /**
     * <p>category</p>
     */
    @NameInMap("category")
    @Validation(required = true)
    public String category;

    @NameInMap("fields")
    public String fields;

    @NameInMap("filter")
    public String filter;

    /**
     * <p>image_thumbnail_process</p>
     */
    @NameInMap("image_thumbnail_process")
    public String imageThumbnailProcess;

    /**
     * <p>image_url_process</p>
     */
    @NameInMap("image_url_process")
    public String imageUrlProcess;

    @NameInMap("limit")
    public Integer limit;

    @NameInMap("marker")
    public String marker;

    /**
     * <p>office_thumbnail_process</p>
     */
    @NameInMap("office_thumbnail_process")
    public String officeThumbnailProcess;

    @NameInMap("order_by")
    public String orderBy;

    @NameInMap("order_direction")
    public String orderDirection;

    @NameInMap("thumbnail_processes")
    public java.util.Map<String, ?> thumbnailProcesses;

    @NameInMap("url_expire_sec")
    public Integer urlExpireSec;

    /**
     * <p>user_id</p>
     */
    @NameInMap("user_id")
    public String userId;

    /**
     * <p>video_thumbnail_process</p>
     * <p>type:string</p>
     */
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    /**
     * <p>view_id</p>
     */
    @NameInMap("view_id")
    @Validation(required = true)
    public String viewId;

    public static ListViewFilesRequest build(java.util.Map<String, ?> map) throws Exception {
        ListViewFilesRequest self = new ListViewFilesRequest();
        return TeaModel.build(map, self);
    }

    public ListViewFilesRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public ListViewFilesRequest setFields(String fields) {
        this.fields = fields;
        return this;
    }
    public String getFields() {
        return this.fields;
    }

    public ListViewFilesRequest setFilter(String filter) {
        this.filter = filter;
        return this;
    }
    public String getFilter() {
        return this.filter;
    }

    public ListViewFilesRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public ListViewFilesRequest setImageUrlProcess(String imageUrlProcess) {
        this.imageUrlProcess = imageUrlProcess;
        return this;
    }
    public String getImageUrlProcess() {
        return this.imageUrlProcess;
    }

    public ListViewFilesRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListViewFilesRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListViewFilesRequest setOfficeThumbnailProcess(String officeThumbnailProcess) {
        this.officeThumbnailProcess = officeThumbnailProcess;
        return this;
    }
    public String getOfficeThumbnailProcess() {
        return this.officeThumbnailProcess;
    }

    public ListViewFilesRequest setOrderBy(String orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public String getOrderBy() {
        return this.orderBy;
    }

    public ListViewFilesRequest setOrderDirection(String orderDirection) {
        this.orderDirection = orderDirection;
        return this;
    }
    public String getOrderDirection() {
        return this.orderDirection;
    }

    public ListViewFilesRequest setThumbnailProcesses(java.util.Map<String, ?> thumbnailProcesses) {
        this.thumbnailProcesses = thumbnailProcesses;
        return this;
    }
    public java.util.Map<String, ?> getThumbnailProcesses() {
        return this.thumbnailProcesses;
    }

    public ListViewFilesRequest setUrlExpireSec(Integer urlExpireSec) {
        this.urlExpireSec = urlExpireSec;
        return this;
    }
    public Integer getUrlExpireSec() {
        return this.urlExpireSec;
    }

    public ListViewFilesRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

    public ListViewFilesRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

    public ListViewFilesRequest setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
