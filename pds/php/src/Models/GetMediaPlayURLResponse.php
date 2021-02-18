<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * get_media_play_url response.
 */
class GetMediaPlayURLResponse extends Model
{
    /**
     * @description url
     *
     * @example https://abc.com/v2/file/play_media?auth_key=xyz&file_id=abc
     *
     * @var string
     */
    public $url;
    protected $_name = [
        'url' => 'url',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->url) {
            $res['url'] = $this->url;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetMediaPlayURLResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['url'])) {
            $model->url = $map['url'];
        }

        return $model;
    }
}
