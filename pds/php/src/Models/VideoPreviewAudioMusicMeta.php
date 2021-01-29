<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class VideoPreviewAudioMusicMeta extends Model {
    protected $_name = [
        'album' => 'album',
        'artist' => 'artist',
        'coverUrl' => 'cover_url',
        'title' => 'title',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->album) {
            $res['album'] = $this->album;
        }
        if (null !== $this->artist) {
            $res['artist'] = $this->artist;
        }
        if (null !== $this->coverUrl) {
            $res['cover_url'] = $this->coverUrl;
        }
        if (null !== $this->title) {
            $res['title'] = $this->title;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return VideoPreviewAudioMusicMeta
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['album'])){
            $model->album = $map['album'];
        }
        if(isset($map['artist'])){
            $model->artist = $map['artist'];
        }
        if(isset($map['cover_url'])){
            $model->coverUrl = $map['cover_url'];
        }
        if(isset($map['title'])){
            $model->title = $map['title'];
        }
        return $model;
    }
    /**
     * @description album
     * @example "范特西"
     * @var string
     */
    public $album;

    /**
     * @description artist
     * @example "周杰伦"
     * @var string
     */
    public $artist;

    /**
     * @description cover_url
     * @example https://ccp.data.aliyuncs.com/hz22%2F5d5b986facbec311ef844c25954f96821497b383%2F5d5b986f955410dd991646bb87c6b4e899eff525?Expires=xxx&OSSAccessKeyId=xxx&Signature=xxx
     * @var string
     */
    public $coverUrl;

    /**
     * @description title
     * @example "爱在西元前"
     * @var string
     */
    public $title;

}
