// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * list_file_by_anonymous request
 */
public class ListByAnonymousRequest extends TeaModel {
    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

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

    // marker
    @NameInMap("marker")
    public String marker;

    // office_thumbnail_process
    @NameInMap("office_thumbnail_process")
    public String officeThumbnailProcess;

    // parent_file_id
    @NameInMap("parent_file_id")
    @Validation(required = true, pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 4)
    public String parentFileId;

    @NameInMap("referer")
    public String referer;

    // share_id
    @NameInMap("share_id")
    @Validation(required = true)
    public String shareId;

    @NameInMap("sign_token")
    public String signToken;

    // video_thumbnail_process
    // type:string
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static ListByAnonymousRequest build(java.util.Map<String, ?> map) throws Exception {
        ListByAnonymousRequest self = new ListByAnonymousRequest();
        return TeaModel.build(map, self);
    }

    public ListByAnonymousRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public ListByAnonymousRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public ListByAnonymousRequest setImageUrlProcess(String imageUrlProcess) {
        this.imageUrlProcess = imageUrlProcess;
        return this;
    }
    public String getImageUrlProcess() {
        return this.imageUrlProcess;
    }

    public ListByAnonymousRequest setLimit(Long limit) {
        this.limit = limit;
        return this;
    }
    public Long getLimit() {
        return this.limit;
    }

    public ListByAnonymousRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListByAnonymousRequest setOfficeThumbnailProcess(String officeThumbnailProcess) {
        this.officeThumbnailProcess = officeThumbnailProcess;
        return this;
    }
    public String getOfficeThumbnailProcess() {
        return this.officeThumbnailProcess;
    }

    public ListByAnonymousRequest setParentFileId(String parentFileId) {
        this.parentFileId = parentFileId;
        return this;
    }
    public String getParentFileId() {
        return this.parentFileId;
    }

    public ListByAnonymousRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public ListByAnonymousRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public ListByAnonymousRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

    public ListByAnonymousRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
