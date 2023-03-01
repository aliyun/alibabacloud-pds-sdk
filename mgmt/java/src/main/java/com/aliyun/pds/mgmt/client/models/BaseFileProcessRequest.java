// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseFileProcessRequest extends TeaModel {
    @NameInMap("image_cropping_aspect_ratios")
    public java.util.List<String> imageCroppingAspectRatios;

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

    /**
     * <p>office_thumbnail_process</p>
     */
    @NameInMap("office_thumbnail_process")
    public String officeThumbnailProcess;

    /**
     * <p>video_thumbnail_process</p>
     * <p>type:string</p>
     */
    @NameInMap("video_thumbnail_process")
    public String videoThumbnailProcess;

    public static BaseFileProcessRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseFileProcessRequest self = new BaseFileProcessRequest();
        return TeaModel.build(map, self);
    }

    public BaseFileProcessRequest setImageCroppingAspectRatios(java.util.List<String> imageCroppingAspectRatios) {
        this.imageCroppingAspectRatios = imageCroppingAspectRatios;
        return this;
    }
    public java.util.List<String> getImageCroppingAspectRatios() {
        return this.imageCroppingAspectRatios;
    }

    public BaseFileProcessRequest setImageThumbnailProcess(String imageThumbnailProcess) {
        this.imageThumbnailProcess = imageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.imageThumbnailProcess;
    }

    public BaseFileProcessRequest setImageUrlProcess(String imageUrlProcess) {
        this.imageUrlProcess = imageUrlProcess;
        return this;
    }
    public String getImageUrlProcess() {
        return this.imageUrlProcess;
    }

    public BaseFileProcessRequest setOfficeThumbnailProcess(String officeThumbnailProcess) {
        this.officeThumbnailProcess = officeThumbnailProcess;
        return this;
    }
    public String getOfficeThumbnailProcess() {
        return this.officeThumbnailProcess;
    }

    public BaseFileProcessRequest setVideoThumbnailProcess(String videoThumbnailProcess) {
        this.videoThumbnailProcess = videoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.videoThumbnailProcess;
    }

}
