// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewAudioMusicMeta extends TeaModel {
    // album
    @NameInMap("album")
    public String album;

    // artist
    @NameInMap("artist")
    public String artist;

    // cover_url
    @NameInMap("cover_url")
    public String coverUrl;

    // title
    @NameInMap("title")
    public String title;

    public static VideoPreviewAudioMusicMeta build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewAudioMusicMeta self = new VideoPreviewAudioMusicMeta();
        return TeaModel.build(map, self);
    }

    public VideoPreviewAudioMusicMeta setAlbum(String album) {
        this.album = album;
        return this;
    }
    public String getAlbum() {
        return this.album;
    }

    public VideoPreviewAudioMusicMeta setArtist(String artist) {
        this.artist = artist;
        return this;
    }
    public String getArtist() {
        return this.artist;
    }

    public VideoPreviewAudioMusicMeta setCoverUrl(String coverUrl) {
        this.coverUrl = coverUrl;
        return this;
    }
    public String getCoverUrl() {
        return this.coverUrl;
    }

    public VideoPreviewAudioMusicMeta setTitle(String title) {
        this.title = title;
        return this;
    }
    public String getTitle() {
        return this.title;
    }

}
