<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取视频雪碧图地址 url response.
 */
class GetVideoPreviewSpriteURLResponse extends Model
{
    /**
     * @description col
     *
     * @example 10
     *
     * @var int
     */
    public $col;

    /**
     * @description count
     *
     * @example 4
     *
     * @var int
     */
    public $count;

    /**
     * @description frame_count
     *
     * @example 450
     *
     * @var int
     */
    public $frameCount;

    /**
     * @description frame_height
     *
     * @example 90
     *
     * @var int
     */
    public $frameHeight;

    /**
     * @description frame_width
     *
     * @example 160
     *
     * @var int
     */
    public $frameWidth;

    /**
     * @description row
     *
     * @example 10
     *
     * @var int
     */
    public $row;

    /**
     * @description sprite_url_list
     *
     * @example [https://ccp.data.aliyuncs.com/hz22%2F5d79219b0aa9a7c995a94a96993ba3205cd91c5a%2F5d79219bf3261a5d38744da0834ed489b677a27a?Expires=xxxOSSAccessKeyId=xxx&Signature=xxx&response-content-disposition=attachment%3Bfilename%3DtBiZAoJPC2c8b13450eda4292b7f5f8010618e078.txt]
     *
     * @var string[]
     */
    public $spriteUrlList;
    protected $_name = [
        'col'           => 'col',
        'count'         => 'count',
        'frameCount'    => 'frame_count',
        'frameHeight'   => 'frame_height',
        'frameWidth'    => 'frame_width',
        'row'           => 'row',
        'spriteUrlList' => 'sprite_url_list',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->col) {
            $res['col'] = $this->col;
        }
        if (null !== $this->count) {
            $res['count'] = $this->count;
        }
        if (null !== $this->frameCount) {
            $res['frame_count'] = $this->frameCount;
        }
        if (null !== $this->frameHeight) {
            $res['frame_height'] = $this->frameHeight;
        }
        if (null !== $this->frameWidth) {
            $res['frame_width'] = $this->frameWidth;
        }
        if (null !== $this->row) {
            $res['row'] = $this->row;
        }
        if (null !== $this->spriteUrlList) {
            $res['sprite_url_list'] = $this->spriteUrlList;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetVideoPreviewSpriteURLResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['col'])) {
            $model->col = $map['col'];
        }
        if (isset($map['count'])) {
            $model->count = $map['count'];
        }
        if (isset($map['frame_count'])) {
            $model->frameCount = $map['frame_count'];
        }
        if (isset($map['frame_height'])) {
            $model->frameHeight = $map['frame_height'];
        }
        if (isset($map['frame_width'])) {
            $model->frameWidth = $map['frame_width'];
        }
        if (isset($map['row'])) {
            $model->row = $map['row'];
        }
        if (isset($map['sprite_url_list'])) {
            if (!empty($map['sprite_url_list'])) {
                $model->spriteUrlList = $map['sprite_url_list'];
            }
        }

        return $model;
    }
}
