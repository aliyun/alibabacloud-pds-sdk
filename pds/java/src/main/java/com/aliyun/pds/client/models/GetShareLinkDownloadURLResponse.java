// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取分享中文件数据response
 */
public class GetShareLinkDownloadURLResponse extends TeaModel {
    // audio_template_list
    @NameInMap("audio_template_list")
    public java.util.List<MediaPlayInfoTemplate> audioTemplateList;

    // download_url
    @NameInMap("download_url")
    public String downloadUrl;

    // @Deprecated streams url info
    @NameInMap("streams_info")
    public java.util.Map<String, ?> streamsInfo;

    // thumbnail
    @NameInMap("thumbnail")
    public String thumbnail;

    // url
    @NameInMap("url")
    public String url;

    // video_template_list
    @NameInMap("video_template_list")
    public java.util.List<MediaPlayInfoTemplate> videoTemplateList;

    public static GetShareLinkDownloadURLResponse build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkDownloadURLResponse self = new GetShareLinkDownloadURLResponse();
        return TeaModel.build(map, self);
    }

    public GetShareLinkDownloadURLResponse setAudioTemplateList(java.util.List<MediaPlayInfoTemplate> audioTemplateList) {
        this.audioTemplateList = audioTemplateList;
        return this;
    }
    public java.util.List<MediaPlayInfoTemplate> getAudioTemplateList() {
        return this.audioTemplateList;
    }

    public GetShareLinkDownloadURLResponse setDownloadUrl(String downloadUrl) {
        this.downloadUrl = downloadUrl;
        return this;
    }
    public String getDownloadUrl() {
        return this.downloadUrl;
    }

    public GetShareLinkDownloadURLResponse setStreamsInfo(java.util.Map<String, ?> streamsInfo) {
        this.streamsInfo = streamsInfo;
        return this;
    }
    public java.util.Map<String, ?> getStreamsInfo() {
        return this.streamsInfo;
    }

    public GetShareLinkDownloadURLResponse setThumbnail(String thumbnail) {
        this.thumbnail = thumbnail;
        return this;
    }
    public String getThumbnail() {
        return this.thumbnail;
    }

    public GetShareLinkDownloadURLResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

    public GetShareLinkDownloadURLResponse setVideoTemplateList(java.util.List<MediaPlayInfoTemplate> videoTemplateList) {
        this.videoTemplateList = videoTemplateList;
        return this;
    }
    public java.util.List<MediaPlayInfoTemplate> getVideoTemplateList() {
        return this.videoTemplateList;
    }

}
