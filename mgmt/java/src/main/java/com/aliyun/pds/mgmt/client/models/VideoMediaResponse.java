// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoMediaResponse extends TeaModel {
    // address_line
    @NameInMap("address_line")
    public String addressLine;

    // city
    @NameInMap("city")
    public String city;

    // country
    @NameInMap("country")
    public String country;

    // district
    @NameInMap("district")
    public String district;

    // duration 单位 秒
    @NameInMap("duration")
    public String duration;

    // height
    @NameInMap("height")
    public Long height;

    // system_tags
    @NameInMap("image_tags")
    public java.util.List<SystemTag> imageTags;

    // location
    @NameInMap("location")
    public String location;

    // province
    @NameInMap("province")
    public String province;

    // time
    @NameInMap("time")
    public String time;

    // township
    @NameInMap("township")
    public String township;

    @NameInMap("video_media_audio_stream")
    public java.util.List<VideoMediaAudioStream> videoMediaAudioStream;

    @NameInMap("video_media_video_stream")
    public java.util.List<VideoMediaVideoStream> videoMediaVideoStream;

    // width
    @NameInMap("width")
    public Long width;

    public static VideoMediaResponse build(java.util.Map<String, ?> map) throws Exception {
        VideoMediaResponse self = new VideoMediaResponse();
        return TeaModel.build(map, self);
    }

    public VideoMediaResponse setAddressLine(String addressLine) {
        this.addressLine = addressLine;
        return this;
    }
    public String getAddressLine() {
        return this.addressLine;
    }

    public VideoMediaResponse setCity(String city) {
        this.city = city;
        return this;
    }
    public String getCity() {
        return this.city;
    }

    public VideoMediaResponse setCountry(String country) {
        this.country = country;
        return this;
    }
    public String getCountry() {
        return this.country;
    }

    public VideoMediaResponse setDistrict(String district) {
        this.district = district;
        return this;
    }
    public String getDistrict() {
        return this.district;
    }

    public VideoMediaResponse setDuration(String duration) {
        this.duration = duration;
        return this;
    }
    public String getDuration() {
        return this.duration;
    }

    public VideoMediaResponse setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public VideoMediaResponse setImageTags(java.util.List<SystemTag> imageTags) {
        this.imageTags = imageTags;
        return this;
    }
    public java.util.List<SystemTag> getImageTags() {
        return this.imageTags;
    }

    public VideoMediaResponse setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public VideoMediaResponse setProvince(String province) {
        this.province = province;
        return this;
    }
    public String getProvince() {
        return this.province;
    }

    public VideoMediaResponse setTime(String time) {
        this.time = time;
        return this;
    }
    public String getTime() {
        return this.time;
    }

    public VideoMediaResponse setTownship(String township) {
        this.township = township;
        return this;
    }
    public String getTownship() {
        return this.township;
    }

    public VideoMediaResponse setVideoMediaAudioStream(java.util.List<VideoMediaAudioStream> videoMediaAudioStream) {
        this.videoMediaAudioStream = videoMediaAudioStream;
        return this;
    }
    public java.util.List<VideoMediaAudioStream> getVideoMediaAudioStream() {
        return this.videoMediaAudioStream;
    }

    public VideoMediaResponse setVideoMediaVideoStream(java.util.List<VideoMediaVideoStream> videoMediaVideoStream) {
        this.videoMediaVideoStream = videoMediaVideoStream;
        return this;
    }
    public java.util.List<VideoMediaVideoStream> getVideoMediaVideoStream() {
        return this.videoMediaVideoStream;
    }

    public VideoMediaResponse setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
