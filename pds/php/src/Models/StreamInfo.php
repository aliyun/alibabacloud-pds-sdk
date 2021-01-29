<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class StreamInfo extends Model {
    protected $_name = [
        'crc64Hash' => 'crc64_hash',
        'downloadUrl' => 'download_url',
        'size' => 'size',
        'thumbnail' => 'thumbnail',
        'url' => 'url',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->crc64Hash) {
            $res['crc64_hash'] = $this->crc64Hash;
        }
        if (null !== $this->downloadUrl) {
            $res['download_url'] = $this->downloadUrl;
        }
        if (null !== $this->size) {
            $res['size'] = $this->size;
        }
        if (null !== $this->thumbnail) {
            $res['thumbnail'] = $this->thumbnail;
        }
        if (null !== $this->url) {
            $res['url'] = $this->url;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return StreamInfo
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['crc64_hash'])){
            $model->crc64Hash = $map['crc64_hash'];
        }
        if(isset($map['download_url'])){
            $model->downloadUrl = $map['download_url'];
        }
        if(isset($map['size'])){
            $model->size = $map['size'];
        }
        if(isset($map['thumbnail'])){
            $model->thumbnail = $map['thumbnail'];
        }
        if(isset($map['url'])){
            $model->url = $map['url'];
        }
        return $model;
    }
    /**
     * @description crc64_hash
     * @var string
     */
    public $crc64Hash;

    /**
     * @description download_url
     * @example https://ccp.data.aliyuncs.com/hz22%2F5d5b986facbec311ef844c25954f96821497b383%2F5d5b986f955410dd991646bb87c6b4e899eff525?Expires=xxx&OSSAccessKeyId=xxx&Signature=xxx
     * @var string
     */
    public $downloadUrl;

    /**
     * @var int
     */
    public $size;

    /**
     * @description thumbnail
     * @example https://ccp.data.aliyuncs.com/hz22%2F5d5b986facbec311ef844c25954f96821497b383%2F5d5b986f955410dd991646bb87c6b4e899eff525?Expires=xxx&OSSAccessKeyId=xxx&Signature=xxx
     * @var string
     */
    public $thumbnail;

    /**
     * @description url
     * @example https://ccp.data.aliyuncs.com/hz22%2F5d5b986facbec311ef844c25954f96821497b383%2F5d5b986f955410dd991646bb87c6b4e899eff525?Expires=xxx&OSSAccessKeyId=xxx&Signature=xxx
     * @var string
     */
    public $url;

}
