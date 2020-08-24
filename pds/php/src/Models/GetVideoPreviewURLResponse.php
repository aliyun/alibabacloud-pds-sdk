<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取视频文件播放 url response.
 */
class GetVideoPreviewURLResponse extends Model
{
    /**
     * @description preview_url
     *
     * @example https://ccp.data.aliyuncs.com/hz22%2F5d79219b0aa9a7c995a94a96993ba3205cd91c5a%2F5d79219bf3261a5d38744da0834ed489b677a27a?Expires=xxxOSSAccessKeyId=xxx&Signature=xxx&response-content-disposition=attachment%3Bfilename%3DtBiZAoJPC2c8b13450eda4292b7f5f8010618e078.txt
     *
     * @var string
     */
    public $previewUrl;
    protected $_name = [
        'previewUrl' => 'preview_url',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->previewUrl) {
            $res['preview_url'] = $this->previewUrl;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetVideoPreviewURLResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['preview_url'])) {
            $model->previewUrl = $map['preview_url'];
        }

        return $model;
    }
}
